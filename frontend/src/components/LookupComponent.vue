<template>
  <main>
    <SearchBar
      v-if="show_search_bar"
      @search="(word) => lookup(word, false)"
    />
    <DottedSpinner v-if="loading" />
    <WordDefinition
      v-if="show_definition"
      @word-lookup="(word) => lookup(word, true)"
      :data="word_data"
    />
  </main>
</template>

<script>
import SearchBar from "./SearchBarComponent.vue";
import DottedSpinner from "./DottedSpinnerComponent.vue";
import WordDefinition from "./WordDefinitionComponent.vue";

export default {
  data() {
    return {
      word_data: [],
      show_search_bar: true,
      loading: false,
      show_definition: false,
    };
  },
  methods: {
    async lookup(word) {
      this.show_search_bar = false;
      this.loading = true;
      this.show_definition = false;

      const form_data = new FormData();
      form_data.append("word", word);

      fetch("http://localhost:5000", {
        method: "POST",
        body: form_data,
      })
        .then((response) => response.json())
        .then((data) => {
          this.word_data = data;
          this.show_definition = true;
        })
        .catch((err) => {
          console.log(err);
        })
        .finally(() => {
          this.show_search_bar = true;
          this.loading = false;
        });
    },
  },
  components: {
    SearchBar: SearchBar,
    DottedSpinner: DottedSpinner,
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
