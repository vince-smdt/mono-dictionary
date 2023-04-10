<template>
  <ul>
    <li
      v-for="(style, name) in items"
      :key="name"
      @click="$emit('item-click', name)"
      :style="style"
    >
      {{ name }}
    </li>
  </ul>
</template>

<script>
export default {
  name: "DropDownList",
  props: {
    items: Object,
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
      filter: brightness(90%);
      transition: filter 0.1s ease-in;
    }
  }
}
</style>
