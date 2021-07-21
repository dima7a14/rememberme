<template>
  <div class="home">
    <h1>RememberMe</h1>
    <phrases-list></phrases-list>
  </div>
</template>

<script>
// @ is an alias to /src
import PhrasesList from '@/components/PhrasesList.vue';

export default {
  name: 'Home',
  components: {
    PhrasesList,
  },
};
</script>
