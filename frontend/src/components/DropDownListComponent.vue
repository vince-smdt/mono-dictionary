<template>
  <ul>
    <li v-for="item in items" :key="item" @click="$emit('item-click', item)">
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

ul {
  list-style: none;
  background: var(--main-color-15);
  border-radius: 5px;
  overflow: hidden;
  li {
    padding: 0.5em 1em;
    cursor: pointer;
    &:hover {
      background: var(--main-color-30);
    }
  }
}
</style>
