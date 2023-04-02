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

<style scoped lang="scss">
@import "../assets/scss/variables.scss";
@import "../assets/scss/functions.scss";

ul {
  list-style: none;
  background: var(--main-color-25);
  border-radius: 5px;
  overflow: hidden;
  li {
    padding: 0.5em 1em;
    cursor: pointer;
    &:hover {
      background: var(--main-color-35);
    }
  }
}
</style>
