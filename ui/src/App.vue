<template>
  <div id="app">
    <!-- Header-->
    <Navbar/>
    <!-- Pages -->
    <component :is="currentPage"/>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
<script>
import Navbar from "./components/Navbar";
import AllDatasets from "./views/AllDatasets";

const PAGE_ALL_DATASETS = 'PAGE_ALL_DATASETS';
const PAGE_DATASET_CONTENTS ='PAGE_DATASET_CONTENTS';
const PAGES = {
  [PAGE_ALL_DATASETS]: AllDatasets,
  [PAGE_DATASET_CONTENTS]: DatasetDetails,
}

export default {
  components: {Navbar},
  data() {
    return {
      currentPage: PAGE_ALL_DATASETS,
    };
  },
  computed: {
      computed: {
        currentPage() {
            return PAGES[this.currentPage]
        }
    },
  }
}
</script>