<template>
  <article>
    <header>
      <h3>Some phrase</h3>
    </header>
    <section>
      <h5>Similar</h5>
      <p>some similar words and phrases</p>
      <h5>Mentions</h5>
      <p>Some mentions of the phrase</p>
      <h5>Translation</h5>
      <p>Translation of the phrase</p>
      <h5>Auto-Translation</h5>
      <p>Auto-Translation of the phrase</p>
    </section>
  </article>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PhraseCard',
});

</script>
