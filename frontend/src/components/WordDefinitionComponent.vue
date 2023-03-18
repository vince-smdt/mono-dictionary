<template>
  <!-- Sense -->
  <div
    v-if="(typeof data === 'object' && data['error'] !== undefined) || !Array.isArray(data)"
    id="error-div"
  >
    <div class="sense">
      Invalid word!
    </div>
  </div>
  <div v-else id="word-sense-list">
    <div class="sense" v-for="(sense, index) in data" :key="sense">
      <!-- Phonetic -->
      <strong class="word">{{ sense.word }}</strong>
      <sup class="sense-index">{{ index + 1 }}</sup>
      <em class="phonetic">{{ sense.phonetic }}</em>
      <br />

      <!-- Meaning -->
      <div class="meaning" v-for="meaning in sense.meanings" :key="meaning">
        <em class="part-of-speech">{{ meaning.partOfSpeech }}</em>

        <!-- Definition -->
        <ul>
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
        </ul>

        <!-- Meaning synonyms -->
        <div v-if="meaning.synonyms.length">
          Synonyms
          <div>
            <span v-for="(synonym, index) in meaning.synonyms" :key="synonym">
              <a class="synonym" @click="$emit('word-lookup', synonym)">{{
                synonym
              }}</a
              ><span v-if="index < meaning.synonyms.length - 1">,&nbsp;</span>
            </span>
          </div>
        </div>

        <!-- Meaning antonyms -->
        <div v-if="meaning.antonyms.length">
          Antonyms
          <div>
            <span v-for="(antonym, index) in meaning.antonyms" :key="antonym">
              <a class="antonym" @click="$emit('word-lookup', antonym)">{{
                antonym
              }}</a
              ><span v-if="index < meaning.antonyms.length - 1">,&nbsp;</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WordDefinition",
  props: {
    data: undefined,
  },
};
</script>

<style scoped>
#error-div,
#word-sense-list {
  max-width: 80em;
  margin: 1em;
}

.sense {
  margin-bottom: 1em;
  padding: 1em;
  border-radius: 10px;
  background: var(--background-light);
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

.meaning {
  margin-bottom: 1em;
}

.part-of-speech {
  font-size: 18px;
}

.synonym,
.antonym {
  font-style: italic;
  text-decoration: underline;
  cursor: pointer;
}

li {
  margin: 0.3em 0 0.3em 3em;
}
</style>
