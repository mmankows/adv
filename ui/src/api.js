import axios from 'axios';
import Vue from 'vue'

const TOAST_DURATION = 6000;

// Create a custom axios instance
const api = axios.create({
    baseURL: `/api`,
    responseType: 'json',
    timeout: 10000,
    headers: {
      'Content-Type': 'application/json'
    }
});


class Resource {
    constructor(resourcePath) {
        this.path = resourcePath;
    }

    async _handler(promise) {
        // Add generic 404, 500, 400 errors handling
        try {
            const resp = await promise;
            return resp.data;
        } catch (e) {
            window.console.log("EXC", e);
            const detail = (e.response.data || {}).detail || '';
            const respCode = e.response.status;

            if (respCode === 400) {
                Vue.toasted.show(`Bad request: ${detail}`, {
                    duration: TOAST_DURATION,
                    type: 'error',
                });
            } else if (respCode === 500) {
                Vue.toasted.show(`Server Error`, {
                    duration: TOAST_DURATION,
                    type: 'error',
                });
            }
            throw e;
        }

    }

    post(path, params = {}) {
        return this._handler(api.post(path, params))
    }

    get(path, params = {}) {
        return this._handler(api.get(path, {params}));
    }

    list() {
        return this.get(`/${this.path}/`);
    }
}


class DatasetResource extends Resource {
    fetchNew() {
        return this.post(`/${this.path}/`);
    }
    contents({id}) {
        return this.get(`/${this.path}/${id}/contents/`);
    }
    groupByCount({id}, [...columnNames]) {
        return this.get(`/${this.path/${id}/groupby_count/}`, {cols: columnNames.join(',')})
    }
}

// Init API Resource
export const Datasets = new DatasetResource('datasets');
