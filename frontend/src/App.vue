<template>
  <header class="m-4 bg-white rounded-xl shadow-md p-6">
    <h1 class="text-center font-semibold text-3xl text-green-600">
      Remember me!
    </h1>
  </header>
  <section class="m-4 bg-gray-200 0 rounded-xl shadow-md w-1/3 mx-auto border-solid border-2 border-gray-300">
    <div
      class="
        rounded-t-xl
        bg-white
        border-solid border-b-2 border-gray-300
        p-3
        h-20
        flex flex-col
        justify-center
        mb-2
      "
    >
      <h2 class="text-center font-light italic text-gray-700 line text-2xl">
        have originated
      </h2>
    </div>
    <div class="p-2">
      <div class="mb-2">
        <h3 class="font-semibold text-grey-700 text-xl">
          Translations
        </h3>
        <ul class="list-disc pl-4">
          <li>Виникли</li>
          <li>З'явилися</li>
        </ul>
      </div>
      <div class="mb-2">
        <h3 class="font-semibold text-grey-700 text-xl">
          Auto-Translations
        </h3>
        <ul class="list-disc pl-4">
          <li>виникли</li>
        </ul>
      </div>
      <div class="mb-2">
        <h3 class="font-semibold text-grey-700 text-xl">
          Similar
        </h3>
        <ul class="list-disc pl-4">
          <li>originate</li>
          <li>tribe</li>
          <li>chow</li>
        </ul>
      </div>
      <div class="mb-2">
        <h3 class="font-semibold text-grey-700 text-xl">
          Mentions
        </h3>
        <ul class="list-disc pl-4">
          <li>The custom is believed to have originated in the western U.S.</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>
