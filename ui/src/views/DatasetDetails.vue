<template>
  <section>
  <h1>Dataset #{{id}} details</h1>
  <div class="float-left py-3">
    <template v-if="!groupByColumns">
      <button type="button" class="btn btn-info mx-2" @click="loadMore">Load more...</button>
      <button type="button" class="btn btn-info mx-2" @click="groupByColumns = []">Group columns...</button>
    </template>
    <template v-else>
        <button
            type="button"
            class="btn btn-info mx-2"
            :disabled="!canLoadGroupBy"
            @click="loadGroupBy">
          Show counts
        </button>
        <button type="button" class="btn btn-danger mx-2" @click="cancelGroupBy">
          {{groupByResultsLoaded ? 'Back' : 'Cancel'}}
        </button>
        <label v-if="!groupByResultsLoaded">
          Toggle columns by clicking on header below: <strong>{{selectedColumnsFormatted}}</strong>
        </label>
        <label v-else>
          Results count grupped by: <strong>{{selectedColumnsFormatted}}</strong>
        </label>
    </template>
  </div>
  <div>
      <SimpleTable
        :header="header"
        :rows="rows"
        @headerClicked="toggleGroupByColumn"
    />
  </div>
  </section>
</template>

<script>
import {PAGES} from "@/constants";
import SimpleTable from "@/components/SimpleTable";
import {Datasets} from "@/api";

const HEADER = [
    'name',
    'height',
    'mass',
    'hair_color',
    'skin_color',
    'eye_color',
    'birth_year',
    'gender',
    'homeworld',
    'date',
];

const GROUP_BY_COL_NAME = 'value';

export default {
    name: "DatasetDetails",
    props: {
      id:  {
        type: Number,
      },
    },
  data() {
    return {
      rows: [],
      header: HEADER,
      groupByColumns: null,
      HEADER,
      PAGES,
    }
  },
  components: {SimpleTable},
  async beforeMount() {
     this.rows = await this.loadDatasetChunk(0);
  },
  computed: {
      canLoadGroupBy() {
          return !this.groupByResultsLoaded && this.groupByColumns.length > 0
      },
      groupByResultsLoaded() {
          return this.header.indexOf(GROUP_BY_COL_NAME) !== -1;
      },
      selectedColumnsFormatted() {
          return this.groupByColumns.join(', ');
      }
  },
  methods: {
    /** Handler for clicking column name.*/
    toggleGroupByColumn(name) {
      if (!this.groupByColumns || this.groupByResultsLoaded) {
        return;
      }

      if (this.groupByColumns.indexOf(name) !== -1) {
        this.groupByColumns = this.groupByColumns.filter(n => n !== name);
      } else {
        this.groupByColumns = [...this.groupByColumns, name];
      }
    },
    /** On Cancel when in group by mode. */
    async cancelGroupBy() {
      this.groupByColumns = null;
      this.rows = await this.loadDatasetChunk(0);
      this.header = HEADER;
    },
    /** Fetch dataset chunk. */
    async loadDatasetChunk(offset) {
      return await Datasets.contents({id: this.id, offset});
    },
    /** Fetch next slice of dataset rows, only in exploring mode. */
    async loadMore() {
      const newCharacters = await this.loadDatasetChunk(this.rows.length);
      this.rows = [...newCharacters, ...this.rows];
    },
    /** Loads group by results from current selection. */
    async loadGroupBy() {
      this.rows = await Datasets.groupByCount({id: this.id, columnNames: this.groupByColumns});
      this.header = [...this.groupByColumns, GROUP_BY_COL_NAME];
    }
  }
}
</script>

