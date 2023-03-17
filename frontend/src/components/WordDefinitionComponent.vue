<template>
  <!-- Sense -->
  <div id="word-sense-list">
    <div class="sense" v-for="(sense, index) in data" :key="sense">
      <!-- Phonetic -->
      <strong class="word">{{ sense.word }}</strong>
      <sup class="sense-index">{{ index + 1 }}</sup>
      <em class="phonetic">{{ sense.phonetic }}</em>
      <br />

      <!-- Meaning -->
      <div v-for="meaning in sense.meanings" :key="meaning">
        <em class="part-of-speech">{{ meaning.partOfSpeech }}</em>

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
      </div>
    </div>
  </div>
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
  margin: 1em;
}

.sense {
  margin-bottom: 1em;
}

.word {
  font-size: 24px;
}

.sense-index {
  margin-left: 0.5em;
}

.phonetic {
  margin-left: 1em;
}

.part-of-speech {
  font-size: 18px;
}

li {
  margin: 0.2em 0 0.2em 3em;
}
</style>
