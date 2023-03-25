<template>
  <main>
    <!-- TODO - When looking up new word, update search bar content -->
    <SearchBar class="searchbar" @search="(word) => lookup(word, false)" />
    <DottedSpinner class="spinner hidden" style="display: none" />
    <WordDefinition
      class="word-definition hidden"
      style="display: none"
      @word-lookup="(word) => lookup(word, true)"
      :data="word_data"
    />
  </main>
</template>

<script>
import SearchBar from "./SearchBarComponent.vue";
import DottedSpinner from "./DottedSpinnerComponent.vue";
import WordDefinition from "./WordDefinitionComponent.vue";
import $ from "jquery";

export default {
  data() {
    return {
      word_data: [],
      ANIMATION_TIME: 500,
    };
  },
  methods: {
    async sleep(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    async lookup(word) {
      await this.set_class_visiblity("word-definition", false, false);
      await this.set_class_visiblity("searchbar", false);
      await this.set_class_visiblity("spinner", true);

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
        })
        .finally(async () => {
          await this.set_class_visiblity("spinner", false);
          await this.set_class_visiblity("searchbar", true, false);
          await this.set_class_visiblity("word-definition", true, false);
        });
    },
    async set_class_visiblity(component_class, show, wait = true) {
      const SELECTOR = "." + component_class;

      if (show) $(SELECTOR).show();

      $(SELECTOR).toggleClass("hidden", !show);

      if (!show) {
        // Stop rendering component when animation stops
        setTimeout(() => {
          $(SELECTOR).hide();
        }, this.ANIMATION_TIME);
      }

      if (wait) await this.sleep(this.ANIMATION_TIME);
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

.searchbar {
  margin: 2em;
}

.searchbar,
.spinner,
.word-definition {
  transition: all 0.5s ease-out;
}

.hidden {
  transform: translate(0, 100px);
  opacity: 0;
}
</style>
