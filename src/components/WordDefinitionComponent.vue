<template>
  <!-- Sense -->
  <div v-if="data_valid" id="error-div">
    <div class="sense">Invalid word!</div>
  </div>
  <div v-else id="word-sense-list">
    <div class="sense" v-for="(sense, index) in data" :key="sense">
      <!-- Phonetic -->
      <!-- TODO - add microphone svg on the opposite side of the word name and make it play the pronunciation of the word 
           (mp3 from api response) -->
      <!-- TODO - maybe add svg pointing to source of information (url found in api response info) -->
      <div class="sense-header">
        <div>
          <strong class="word">{{ sense.word }}</strong>
          <sup class="sense-index">{{ index + 1 }}</sup>
          <em class="phonetic">{{ sense.phonetic }}</em>
        </div>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            fill="currentColor"
            class="bi bi-mic-fill"
            viewBox="0 0 16 16"
            v-if="
              Array.isArray(sense.phonetics) &&
              ((sense.phonetics[0] && sense.phonetics[0].audio) ||
                (sense.phonetics[1] && sense.phonetics[1].audio))
            "
            @click="
              play_sound(sense.phonetics[0].audio || sense.phonetics[1].audio)
            "
          >
            <path d="M5 3a3 3 0 0 1 6 0v5a3 3 0 0 1-6 0V3z" />
            <path
              d="M3.5 6.5A.5.5 0 0 1 4 7v1a4 4 0 0 0 8 0V7a.5.5 0 0 1 1 0v1a5 5 0 0 1-4.5 4.975V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0 1 .5-.5z"
            />
          </svg>
        </div>
      </div>

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
  methods: {
    play_sound(url) {
      new Audio(url).play();
    },
  },
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

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

#error-div,
#word-sense-list {
  max-width: 60em;
  margin: 0 1em;
}

#word-sense-list {
  li {
    list-style-type: circle;
    margin: 0.5em 0 0.5em 3em;
  }
  .sense {
    margin-bottom: 1em;
    padding: 1em;
    border-radius: 10px;
    background: var(--main-color-5);
    .sense-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      svg:hover {
        transition: fill 0.1s ease-in;
        fill: var(--secondary-color-30);
        cursor: pointer;
      }
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
      .part-of-speech {
        font-size: 18px;
      }
      .definitions {
        margin-bottom: 1em;
        .definition-synonyms,
        .definition-antonyms {
          margin: 0.5em 0;
        }
        .example {
          border-left: var(--secondary-color-15) 3px solid;
          background: var(--main-color-10);
          padding: 0.5em;
          margin: 0.4em 0;
        }
      }
      .meaning-synonyms,
      .meaning-antonyms {
        margin-bottom: 0.5em;
      }
    }
  }
}
</style>
