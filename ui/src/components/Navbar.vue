<template>
    <div id="nav">
      Welcome to Star Wars Explorer
      <button
          type="button"
          class="btn btn-link"
          @click="$emit('navChange', PAGES.ALL_DATASETS)"
      >Datasets</button>
    </div>
</template>

<script>
import {PAGES} from '@/constants';

export default {
    name: "Navbar",
    data() {
      return {
        PAGES,
      }
    },
}
</script>

<style scoped>
  #nav {
    position: fixed;
    width: 100%;
    background: gainsboro;
    padding: 1em;
    height: 4em;
    font-weight: bold;
  }
</style>
