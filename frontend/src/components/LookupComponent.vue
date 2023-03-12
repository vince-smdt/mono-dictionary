<template>
  <main>
    <SearchBar @search="(word) => lookup(word)" />
    <WordDefinition :data="word_data" />
  </main>
</template>

<script>
import SearchBar from "./SearchBarComponent.vue";
import WordDefinition from "./WordDefinitionComponent.vue";

export default {
  data() {
    return {
      word_data: [],
    };
  },
  methods: {
    lookup(word) {
      const form_data = new FormData();
      form_data.append("word", word);

      fetch("http://localhost:5000", {
        method: "POST",
        body: form_data,
      })
        .then((response) => response.json())
        .then((data) => {
          this.word_data = data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  components: {
    SearchBar: SearchBar,
    WordDefinition: WordDefinition,
  },
};
</script>

<style scoped>
main {
  min-height: 100vh;

  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
</style>
