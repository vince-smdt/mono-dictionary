<template>
  <!-- Sense -->
  <div v-if="data_valid" id="error-div">
    <div class="sense">Invalid word!</div>
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
        <ul class="definitions">
          <li v-for="definition in meaning.definitions" :key="definition">
            {{ definition.definition }}

            <!-- Definition synonyms -->
            <div class="definition-synonyms" v-if="definition.synonyms.length">
              Synonyms:
              <WordList
                :data="definition.synonyms"
                @word-clicked="(synonym) => $emit('word-lookup', synonym)"
              />
            </div>

            <!-- Definition antonyms -->
            <div class="definition-antonyms" v-if="definition.antonyms.length">
              Antonyms:
              <WordList
                :data="definition.antonyms"
                @word-clicked="(antonym) => $emit('word-lookup', antonym)"
              />
            </div>

            <!-- Definition example -->
            <blockquote class="example" v-if="'example' in definition">
              Example: {{ definition.example }}
            </blockquote>
          </li>
        </ul>

        <!-- Meaning synonyms -->
        <div class="meaning-synonyms" v-if="meaning.synonyms.length">
          Synonyms:
          <WordList
            :data="meaning.synonyms"
            @word-clicked="(synonym) => $emit('word-lookup', synonym)"
          />
        </div>

        <!-- Meaning antonyms -->
        <div class="meaning-antonyms" v-if="meaning.antonyms.length">
          Antonyms:
          <WordList
            :data="meaning.antonyms"
            @word-clicked="(antonym) => $emit('word-lookup', antonym)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import WordList from "./WordListComponent.vue";

export default {
  name: "WordDefinition",
  props: {
    data: undefined,
  },
  computed: {
    data_valid() {
      return (
        (typeof this.data === "object" && this.data["error"] !== undefined) ||
        !Array.isArray(this.data)
      );
    },
  },
  components: {
    WordList: WordList,
  },
};
</script>

<style scoped>
#error-div,
#word-sense-list {
  max-width: 60em;
  width: 60em;
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

.definitions {
  margin-bottom: 1em;
}

.definition-synonyms,
.definition-antonyms {
  margin: 0.5em 0;
}

.example {
  border-left: var(--blockquote) 3px solid;
  background: var(--background-lighter);
  padding: 0.5em;
  margin: 0.4em 0;
}

.meaning-synonyms,
.meaning-antonyms {
  margin-bottom: 0.5em;
}

li {
  list-style-type: circle;
  margin: 0.5em 0 0.5em 3em;
}
</style>
