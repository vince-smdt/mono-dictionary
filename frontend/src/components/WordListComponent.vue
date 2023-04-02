<template>
  <div>
    <span v-for="(word, index) in data" :key="word">
      <a class="clickable-word" @click="$emit('word-clicked', word)">{{
        word
      }}</a
      ><span v-if="index < data.length - 1">,&nbsp;</span>
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
@import "../assets/scss/functions.scss";

.clickable-word {
  font-style: italic;
  text-decoration: underline;
  cursor: pointer;
}

.clickable-word:hover {
  transition: color 0.1s ease-in;
  color: brightness($secondary-color, -15%);
}
</style>
