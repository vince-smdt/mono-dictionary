<template>
  <ul>
    <li v-for="item in items" :key="item">
      {{ item }}
    </li>
  </ul>
</template>

<script>
export default {
  name: "DropDownList",
  props: {
    items: Array,
  },
};
</script>

<style scoped>
ul {
  list-style: none;
  background: var(--background-nav-dropdown);
  border-radius: 5px;
  overflow: hidden;
}

li {
  padding: 0.5em 1em;
  cursor: pointer;
}

li:hover {
  background: var(--background-nav-dropdown-hover);
}
</style>
