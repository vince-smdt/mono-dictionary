<template>
  <!-- TODO - Add links, github? add underline to links -->
  <footer>
    <div>Developed by <strong>Vincent Simard-Schmidt</strong></div>
    <div class="small-text">
      Powered by
      <a
        href="https://github.com/meetDeveloper/freeDictionaryAPI"
        target="_blank"
      >
        Free Dictionary API
      </a>
    </div>
    <div class="small-text"><i>2023</i></div>
  </footer>
</template>

<script scoped>
export default {
  name: "FooterBar",
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

footer {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background: var(--main-color-10);
  padding: 4em;
  div {
    padding: 0.1em;
    text-align: center;
    strong {
      white-space: nowrap;
    }
  }
  a {
    color: var(--secondary-color);
    &:hover {
      transition: color 0.1s ease-in;
      color: var(--secondary-color-40);
    }
  }
  .small-text {
    font-size: 13px;
  }
}
</style>
