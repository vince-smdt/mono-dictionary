<template>
  <!-- Sense -->
  <div v-if="data_valid" id="error-div">
    <div class="sense">Invalid word!</div>
  </div>
  <div v-else id="word-sense-list">
    <div class="sense" v-for="(sense, index) in data" :key="sense">
      <!-- Phonetic -->
      <div class="sense-header">
        <div>
          <!-- TODO - do something about words overflowing, escpecially on mobile (break-word), ex. pneumonoultramicroscopicsilicovolcanoconiosis -->
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
              sense.phonetics.some((phonetic) => phonetic.audio)
            "
            @click="
              () => {
                let phonetic = sense.phonetics.find(
                  (phonetic) => phonetic.audio
                );
                play_sound(phonetic.audio);
              }
            "
          >
            <path d="M5 3a3 3 0 0 1 6 0v5a3 3 0 0 1-6 0V3z" />
            <path
              d="M3.5 6.5A.5.5 0 0 1 4 7v1a4 4 0 0 0 8 0V7a.5.5 0 0 1 1 0v1a5 5 0 0 1-4.5 4.975V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0 1 .5-.5z"
            />
          </svg>
          <a
            v-if="sense.sourceUrls[0]"
            :href="sense.sourceUrls[0]"
            target="_blank"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              fill="currentColor"
              class="bi bi-globe"
              viewBox="0 0 16 16"
            >
              <path
                d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm7.5-6.923c-.67.204-1.335.82-1.887 1.855A7.97 7.97 0 0 0 5.145 4H7.5V1.077zM4.09 4a9.267 9.267 0 0 1 .64-1.539 6.7 6.7 0 0 1 .597-.933A7.025 7.025 0 0 0 2.255 4H4.09zm-.582 3.5c.03-.877.138-1.718.312-2.5H1.674a6.958 6.958 0 0 0-.656 2.5h2.49zM4.847 5a12.5 12.5 0 0 0-.338 2.5H7.5V5H4.847zM8.5 5v2.5h2.99a12.495 12.495 0 0 0-.337-2.5H8.5zM4.51 8.5a12.5 12.5 0 0 0 .337 2.5H7.5V8.5H4.51zm3.99 0V11h2.653c.187-.765.306-1.608.338-2.5H8.5zM5.145 12c.138.386.295.744.468 1.068.552 1.035 1.218 1.65 1.887 1.855V12H5.145zm.182 2.472a6.696 6.696 0 0 1-.597-.933A9.268 9.268 0 0 1 4.09 12H2.255a7.024 7.024 0 0 0 3.072 2.472zM3.82 11a13.652 13.652 0 0 1-.312-2.5h-2.49c.062.89.291 1.733.656 2.5H3.82zm6.853 3.472A7.024 7.024 0 0 0 13.745 12H11.91a9.27 9.27 0 0 1-.64 1.539 6.688 6.688 0 0 1-.597.933zM8.5 12v2.923c.67-.204 1.335-.82 1.887-1.855.173-.324.33-.682.468-1.068H8.5zm3.68-1h2.146c.365-.767.594-1.61.656-2.5h-2.49a13.65 13.65 0 0 1-.312 2.5zm2.802-3.5a6.959 6.959 0 0 0-.656-2.5H12.18c.174.782.282 1.623.312 2.5h2.49zM11.27 2.461c.247.464.462.98.64 1.539h1.835a7.024 7.024 0 0 0-3.072-2.472c.218.284.418.598.597.933zM10.855 4a7.966 7.966 0 0 0-.468-1.068C9.835 1.897 9.17 1.282 8.5 1.077V4h2.355z"
              />
            </svg>
          </a>
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
      div:nth-of-type(2) > * {
        margin-left: 0.5em;
      }
      svg {
        transition: fill 0.1s ease-in;
        &:hover {
          fill: var(--secondary-color-30);
          cursor: pointer;
        }
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
