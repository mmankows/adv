<template>
  <div id="app">
    <!-- Header-->
    <Navbar @navChange="goToPage"/>
    <!-- Pages -->
    <div id="content">
      <component
          @navChange="goToPage"
          :is="currentPageComponent"
          v-bind="currentPage.props"
      />
    </div>
    <!-- Footer -->
    <footer id="footer">
      Github:
      <a
          class="stretched-link"
          href="https://github.com/mmankows/adv">https://github.com/mmankows/adv
      </a>
    </footer>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  //color: #002200;
}

</style>
<script>
import Navbar from "@/components/Navbar";
import AllDatasets from "@/views/AllDatasets";
import DatasetDetails from "@/views/DatasetDetails";
import {PAGES} from "@/constants";

const PAGES_MAP = {
  [PAGES.ALL_DATASETS]: AllDatasets,
  [PAGES.DATASET_CONTENTS]: DatasetDetails,
}

export default {
  components: {
    Navbar,
    AllDatasets,
    DatasetDetails,
  },
  data() {
    return {
      currentPage: {
          id: PAGES.ALL_DATASETS,
          props: {}
      },
    };
  },
  computed: {
      currentPageComponent() {
          return PAGES_MAP[this.currentPage.id]
      }
  },
  methods: {
    goToPage(id, props = {}) {
        this.currentPage = {id, props};
    }
  }
}
</script>


<style scoped>
  #content {
    padding-top: 4em;
  }
  #footer {
    padding-top: 2rem;
    padding-bottom: 1rem;
    background: black;
    color: gainsboro;
  }
</style>