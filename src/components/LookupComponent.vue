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
      // Scroll back up to top of window
      window.scrollTo({top: 0, behavior: 'smooth'});

      // Unfocus and update search bar with word
      this.$refs.searchbar.blur();
      this.$refs.searchbar.update_input(word);

      // Hide search bar and word definition
      await this.set_class_visibility("word-definition", false, false, false);
      await this.set_class_visibility("searchbar", false);

      // Empty word data to avoid spinner misplacement
      this.word_data = "";

      // Show spinner
      await this.set_class_visibility("spinner", true);

      let word_data_holder;
      let url =
        "https://api.dictionaryapi.dev/api/v2/entries/en/" +
        encodeURIComponent(word);

      // Fetch word data
      fetch(url, { method: "GET" })
        .then((response) => response.json())
        .then((data) => {
          word_data_holder = data;
        })
        .catch((err) => {
          this.word_data = { error: err };
        })
        .finally(async () => {
          // Hide spinner
          await this.set_class_visibility("spinner", false);

          // Assign data after spinner animation end to avoid janky spinner movement
          this.word_data = word_data_holder;

          // Show search bar and word definition
          await this.set_class_visibility("searchbar", true, false);
          await this.set_class_visibility("word-definition", true, false);
        });
    },
    async set_class_visibility(
      component_class,
      show,
      wait = true,
      display_none = true
    ) {
      const SELECTOR = "." + component_class;

      if (show) $(SELECTOR).show();

      $(SELECTOR).toggleClass("hidden", !show);

      if (!show && display_none) {
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

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

main {
  min-height: calc(100vh - $header-height);
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

.word-definition {
  min-height: 5em;
}

.hidden {
  transform: translate(0, 100px);
  opacity: 0;
}
</style>
