<template>
  <main>
    <SearchBar @search="(word) => lookup(word)" />
    <div id="word-data">{{ word_data }}</div>
  </main>
</template>

<script>
import SearchBar from "./SearchBarComponent.vue";

export default {
  data() {
    return {
      word_data: "",
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
          this.word_data = JSON.stringify(data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  components: {
    SearchBar: SearchBar,
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

#word-data {
  margin: 5px 0;
  padding: 10px;
  color: white;
}
</style>
