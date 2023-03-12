<template>
  <ol id="outer-list">
    <li v-for="sense in data" :key="sense">
      {{ sense.word }}, phonetic: <span>{{ sense.phonetic }}</span>
      <ol>
        <li v-for="meaning in sense.meanings" :key="meaning">
          part of speech: {{ meaning.partOfSpeech }}
          <ol>
            <li v-for="definition in meaning.definitions" :key="definition">
              {{ definition.definition }}
            </li>
          </ol>
        </li>
      </ol>
    </li>
  </ol>
</template>

<script>
export default {
  name: "WordDefinition",
  props: {
    data: Array,
  },
};
</script>

<style scoped>
#outer-list {
  max-width: 80em;
}

ol {
  list-style-type: none;
  counter-reset: item;
  margin: 0;
  padding: 0;
}

ol > li {
  display: table;
  counter-increment: item;
  margin-bottom: 0.6em;
}

ol > li:before {
  content: counters(item, ".") ". ";
  display: table-cell;
  padding-right: 0.6em;    
}

li ol > li {
  margin: 0;
}

li ol > li:before {
  content: counters(item, ".") " ";
}

span {
  font-family: "Times New Roman", Times, serif;
}
</style>
