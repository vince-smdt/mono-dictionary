<template>
  <div id="outer-word-list">
    <span v-for="(word, index) in data" :key="word">
      <a class="clickable-word" @click="$emit('word-clicked', word)">
        {{ word }}
      </a>
      <span v-if="index < data.length - 1">,&nbsp;</span>
    </span>
  </div>
</template>

<script>
export default {
  name: "WordList",
  props: {
    data: Array,
  },
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

#outer-word-list {
  span {
    display: inline-block;
  }
  .clickable-word {
    font-style: italic;
    text-decoration: underline;
    cursor: pointer;
    &:hover {
      color: var(--secondary-color-30);
    }
  }
}
</style>
