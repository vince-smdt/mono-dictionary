<template>
  <!-- Sense -->
  <ol id="word-sense-list">
    <li v-for="sense in data" :key="sense">

      <!-- Phonetic -->
      {{ sense.word }}, phonetic:
      <span id="phonetic">{{ sense.phonetic }}</span>

      <!-- Meaning -->
      <ol>
        <li v-for="meaning in sense.meanings" :key="meaning">
          part of speech: {{ meaning.partOfSpeech }}

          <!-- Definition -->
          <ol>
            <li v-for="definition in meaning.definitions" :key="definition">
              {{ definition.definition }}

              <!-- Definition synonyms -->
              <div v-if="definition.synonyms.length">
                Synonyms
                <ul>
                  <li v-for="synonym in definition.synonyms" :key="synonym">
                    {{ synonym }}
                  </li>
                </ul>
              </div>

              <!-- Definition antonyms -->
              <div v-if="definition.antonyms.length">
                Antonyms
                <ul>
                  <li v-for="antonym in definition.antonyms" :key="antonym">
                    {{ antonym }}
                  </li>
                </ul>
              </div>

              <!-- Definition example -->
              <span v-if="'example' in definition">
                Example: {{ definition.example }}
              </span>
            </li>
          </ol>

          <!-- Meaning synonyms -->
          <div v-if="meaning.synonyms.length">
            Synonyms
            <ul>
              <li v-for="synonym in meaning.synonyms" :key="synonym">
                {{ synonym }}
              </li>
            </ul>
          </div>

          <!-- Meaning antonyms -->
          <div v-if="meaning.antonyms.length">
            Antonyms
            <ul>
              <li v-for="antonym in meaning.antonyms" :key="antonym">
                {{ antonym }}
              </li>
            </ul>
          </div>

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
#word-sense-list {
  max-width: 80em;
}

#phonetic {
  font-family: "Times New Roman", Times, serif;
  font-size: 22px;
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

ul > li {
  margin-left: 2em;
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
</style>
