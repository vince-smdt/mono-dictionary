<template>
  <div id="outer-search-bar">
    <label>Word to lookup: </label>
    <div id="search-bar">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        id="bi-search"
        viewBox="0 0 16 16"
      >
        <path
          d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
        />
      </svg>
      <input
        id="search-bar-input"
        ref="search-bar-input"
        type="text"
        v-model="word"
        placeholder="Word to lookup"
        @keydown.esc="$event.target.blur()"
        @input="
          () => {
            if (!prevent_autocomplete_update) {
              update_autocomplete();
              this.typed_word = word.toLowerCase();
              this.focused_suggestion_index = -1;
            }
          }
        "
        @focus="
          () => {
            focused = true;
            update_autocomplete();
            this.typed_word = word.toLowerCase();
          }
        "
        @blur="focused = false"
      />
      <div
        id="suggestions"
        v-if="focused && auto_complete_suggestions.length > 0"
      >
        <a
          v-for="(suggestion, index) in auto_complete_suggestions"
          :key="suggestion"
          @mousedown="
            () => {
              update_input(suggestion);
              search(word);
            }
          "
          :class="index == focused_suggestion_index ? 'suggestion-focus' : ''"
        >
          <b>{{ typed_word }}</b
          >{{ suggestion.substring(typed_word.length) }}
        </a>
      </div>
    </div>
    <button type="button" id="lookup-button" @click="search">Look up</button>
  </div>
</template>

<script>
import words from "../assets/data/words.js";
import utils from "../utils.js";

export default {
  name: "SearchBar",
  mounted() {
    // Setup auto-complete
    this.word_list = words;

    // Event listener for when enter key pressed
    const searchbar = document.getElementById("search-bar");
    searchbar.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        this.search();
      }
    });

    // Setup event listeners for arrow keys and escape
    document
      .getElementById("search-bar-input")
      .addEventListener("keydown", (event) => {
        if (
          this.auto_complete_suggestions.length === 0 ||
          (event.key !== "ArrowDown" && event.key !== "ArrowUp")
        ) {
          this.prevent_autocomplete_update = false;
          return;
        }

        // Prevent up and down arrow keys from changing cursor position
        event.preventDefault();

        // Get function to modify suggestion index
        let index_func = {
          ArrowDown: utils.increment_index_in_range,
          ArrowUp: utils.decrement_index_in_range,
        }[event.key];

        // Modify suggestion index
        this.focused_suggestion_index = index_func(
          this.focused_suggestion_index,
          -1,
          this.auto_complete_suggestions.length - 1
        );

        // Update input
        if (this.focused_suggestion_index !== -1) {
          this.update_input(
            this.auto_complete_suggestions[this.focused_suggestion_index]
          );
        } else {
          // If no suggestions focused on, go back to original word
          this.word = this.typed_word;
        }

        // Do not modify auto complete suggestions upon changing index
        this.prevent_autocomplete_update = true;
      });
  },
  data() {
    return {
      word: "",
      typed_word: "",
      word_list: [],
      auto_complete_suggestions: [],
      MAX_SUGGESTIONS: 10,
      focused: false,
      focused_suggestion_index: -1,
      prevent_autocomplete_update: false,
    };
  },
  methods: {
    update_input(word) {
      this.word = word;
    },
    search() {
      this.$emit("search", this.word);
      this.typed_word = this.word.toLowerCase();
    },
    blur() {
      this.$refs["search-bar-input"].blur();
    },
    focus() {
      this.$refs["search-bar-input"].focus();
    },
    update_autocomplete() {
      let current_word = this.word.toLowerCase();
      this.auto_complete_suggestions = [];

      // No suggestions if word is less than 2 chars long
      if (current_word.length < 2) {
        return;
      }

      // Get auto complete suggestions from word list
      this.word_list.every((word) => {
        if (word.startsWith(current_word)) {
          this.auto_complete_suggestions.push(word);
          if (this.auto_complete_suggestions.length >= this.MAX_SUGGESTIONS) {
            return false; // break out of "every" loop
          }
        }
        return true; // loop
      });
    },
  },
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

#outer-search-bar > * {
  white-space: nowrap;
}

#outer-search-bar label {
  display: none;
  @media screen and (min-width: #{$mobile-width}) {
    display: inline;
  }
}

#outer-search-bar label,
#search-bar input,
#lookup-button {
  font-size: 20px;
  font-family: "Roboto Mono";
  color: var(--secondary-color);
}

#outer-search-bar,
#search-bar {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

#search-bar {
  padding: 5px;
  border: var(--secondary-color) solid 2px;
  border-radius: 5px;
  &:hover {
    background: var(--main-color-5);
  }
  input {
    background: transparent;
    color: var(--secondary-color);
    border: none;
    width: 100%;
    box-sizing: border-box;
    &::placeholder {
      color: var(--secondary-color);
      opacity: 50%;
      @media screen and (min-width: #{$mobile-width}) {
        opacity: 0%;
      }
    }
    &:focus {
      outline: none;
    }
  }
  #suggestions {
    position: absolute;
    top: calc($header-height - 0.67em);
    width: 100%;
    left: 0;
    background: var(--main-color-5);
    outline: var(--secondary-color) solid 2px;
    border-radius: 0 0 5px 5px;
    & > a {
      padding: 0.5em;
      cursor: pointer;
      display: block;
      overflow: hidden;
      text-overflow: ellipsis;
      &.suggestion-focus,
      &:hover {
        background: var(--main-color-15);
      }
    }
  }
}

#lookup-button {
  color: var(--secondary-color);
  background: transparent;
  border: var(--secondary-color) solid 2px;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
  &:hover {
    background: var(--main-color-5);
  }
}
</style>
