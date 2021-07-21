<template>
  <div class="phrases-list">
    <div v-for="phrase in phrases" :key="phrase.id">
      <phrase-card></phrase-card>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import { Api } from "@/api";
import { Phrases } from "@/api/types";
import PhraseCard from "./PhraseCard.vue";

type Data = {
  phrases: Phrases.Phrase[];
};

type Methods = {
  fetch(): Promise<void>;
};

const api = Api.getInstance();

export default defineComponent<
  Record<string, never>,
  Record<string, never>,
  Data,
  Record<string, never>,
  Methods
>({
  name: "PhrasesList",
  components: {
    PhraseCard,
  },
  data() {
    return {
      phrases: [],
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    async fetch() {
      const phrases = await api.phrases.list();

      this.phrases = phrases;
    },
  },
});
</script>
