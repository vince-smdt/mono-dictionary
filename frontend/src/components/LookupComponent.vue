<template>
  <main>
    <div id="input-div">
      <label>Word to lookup: </label>
      <div id="search-bar">
        <img src="../assets/search.svg" alt="Search Icon" />
        <input id="word-input" type="text" v-model="word" />
      </div>
      <button type="button" id="lookup-button" @click="lookup()">
        Look up
      </button>
    </div>

    <div id="word-data">{{ word_data }}</div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      word: "",
      word_data: "",
    };
  },
  methods: {
    lookup() {
      const form_data = new FormData();
      form_data.append("word", this.word);

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

hr {
  margin: 10px 0;
}

#input-div label,
#word-input,
#lookup-button {
  font-size: 20px;
  font-family: "Roboto Mono";
  color: white;
}

#input-div,
#search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

#search-bar {
  padding: 5px;
  border: white solid 2px;
  border-radius: 5px;
}

#search-bar:hover {
  background: #0c2146;
}

#search-bar input {
  background: transparent;
  color: white;
  border: none;
}

#search-bar input:focus {
  outline: none;
}

#lookup-button {
  background: transparent;
  border: white solid 2px;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
}

#lookup-button:hover {
  background: #0c2146;
}

#word-data {
  margin: 5px 0;
  padding: 10px;
  color: white;
}
</style>
