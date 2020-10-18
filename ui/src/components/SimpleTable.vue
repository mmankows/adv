<template>
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th v-for="name in header"
              :key="name"
              scope="col"
              @click="$emit('headerClicked', name)">
              {{name}}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, idx) in rows"
            :key="idx"
            @click="$emit('rowClicked', row)"
            :class="{rowsClickable}">
          <td v-for="name in header"
              :key="name">
                {{ row[name] }}
          </td>
        </tr>
      </tbody>
    </table>
</template>

<script>
export default {
    name: "SimpleTable",
    props: {
      header:  {
        required: true,
        type: Array,
      },
      rows: {
        required: true,
        type: Array,
      },
      rowsClickable: {
        type: Boolean,
      }
    },
}
</script>

<style scoped>
  .rowsClickable {
      color: cornflowerblue;
  }
  .rowsClickable:hover {
      text-decoration: underline;
  }
</style>
