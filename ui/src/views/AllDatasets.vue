<template>
  <section>
    <h1>All Datasets</h1>
    <div class="float-left py-3">
       <button type="button" class="btn btn-info mx-2" @click="fetchNew">Fetch new</button>
    </div>
    <div>
        <SimpleTable
          :header="HEADER"
          :rows="datasets"
          @rowClicked="data => $emit('navChange', PAGES.DATASET_CONTENTS, data)"
      />
    </div>
  </section>
</template>

<script>
import SimpleTable from "@/components/SimpleTable";
import {Datasets} from "@/api";
import {PAGES} from "@/constants";

const HEADER = ['id', 'fetched_timestamp']

export default {
  name: "AllDatasets",
  data() {
    return {
      datasets: [],
      HEADER,
      PAGES,
    }
  },
  components: {SimpleTable},
  async beforeMount() {
     await this.reloadDatasets();
  },
  methods: {
    async reloadDatasets() {
      this.datasets = await Datasets.list();
    },
    async fetchNew() {
      await Datasets.fetchNew();
      await this.reloadDatasets();
    }
  }
}
</script>
