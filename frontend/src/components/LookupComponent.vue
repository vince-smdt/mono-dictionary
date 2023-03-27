<template>
  <main>
    <SearchBar
      ref="searchbar"
      class="searchbar"
      @search="(word) => lookup(word, false)"
    />
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
  mounted() {
    this.focus_searchbar();
  },
  methods: {
    async sleep(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
    async lookup(word) {
      this.$refs.searchbar.update_input(word);

      await this.set_class_visibility("word-definition", false, false);
      await this.set_class_visibility("searchbar", false);
      await this.set_class_visibility("spinner", true);

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
          this.word_data = { error: err };
        })
        .finally(async () => {
          await this.set_class_visibility("spinner", false);
          await this.set_class_visibility("searchbar", true, false);
          await this.set_class_visibility("word-definition", true, false);
          this.focus_searchbar();
        });
    },
    async set_class_visibility(component_class, show, wait = true) {
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
    focus_searchbar() {
      this.$refs.searchbar.focus();
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
