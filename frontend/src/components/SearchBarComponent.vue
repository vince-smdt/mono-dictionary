<template>
  <div id="outer-search-bar">
    <label>Word to lookup: </label>
    <div id="search-bar">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" id="bi-search" viewBox="0 0 16 16">
        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
      </svg>
      <input ref="searchbar-input" type="text" v-model="word" />
    </div>
    <button type="button" id="lookup-button" @click="search">Look up</button>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  mounted() {
    const searchbar = document.getElementById("search-bar");
    searchbar.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        this.search();
      }
    });
  },
  data() {
    return {
      word: "",
    };
  },
  methods: {
    update_input(word) {
      this.word = word;
    },
    search() {
      this.$emit("search", this.word);
    },
    focus() {
      this.$refs["searchbar-input"].focus();
    }
  },
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";
@import "../assets/scss/functions.scss";

#outer-search-bar > * {
  white-space: nowrap;
}

#outer-search-bar label,
#search-bar input,
#lookup-button {
  font-size: 20px;
  font-family: "Roboto Mono";
  color: $secondary-color;
}

#outer-search-bar,
#search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

#search-bar {
  padding: 5px;
  border: $secondary-color solid 2px;
  border-radius: 5px;
  transition: background 0.15s ease-in;
}

#search-bar:hover {
  background: brightness($main-color, 10%);
}

#search-bar input {
  background: transparent;
  color: $secondary-color;
  border: none;
}

#search-bar input:focus {
  outline: none;
}

#lookup-button {
  color: $secondary-color;
  background: transparent;
  border: $secondary-color solid 2px;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
  transition: background 0.15s ease-in;
}

#lookup-button:hover {
  background: brightness($main-color, 10%);
}
</style>
