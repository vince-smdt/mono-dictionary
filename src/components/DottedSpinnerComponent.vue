<template>
  <div class="lds-default">
    <div v-for="i in 12" :key="i"></div>
  </div>
</template>

<script>
export default {
  name: "DottedSpinner",
};
</script>

<style scoped lang="scss">
@import "../assets/scss/variables.scss";

$tops: 37px, 22px, 11px, 7px, 11px, 22px, 37px, 52px, 62px, 66px, 62px, 52px;
$lefts: 66px, 62px, 52px, 37px, 22px, 11px, 7px, 11px, 22px, 37px, 52px, 62px;

.lds-default {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
  div {
    position: absolute;
    width: 6px;
    height: 6px;
    background: var(--secondary-color);
    border-radius: 50%;
    animation: lds-default 1.2s linear infinite;
    @for $i from 1 through 12 {
      &:nth-child(#{$i}) {
        animation-delay: #{($i - 1) * -0.1}s;
        top: nth($tops, $i);
        left: nth($lefts, $i);
      }
    }
  }
}

@keyframes lds-default {
  0%,
  20%,
  80%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.5);
  }
}
</style>
