<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12>
        <div class="tabs-block">
          <v-chip v-model="chip1" close color="blue darken-4" label outline>Dashboard </v-chip>
          <v-chip v-model="chip2" close color="blue darken-4" label outline>Tab </v-chip>
          <v-chip v-model="chip3" close color="blue darken-4" label outline>Tab size </v-chip>
          <v-chip v-model="chip4" close color="blue darken-4" label outline>New tab opend</v-chip>
          <v-chip v-model="chip5" close color="blue darken-4" label outline >Complete</v-chip>
        </div>
      </v-flex>
    </v-layout>
  </div>
</template>


<script>
export default {
  data() {
    return {
      chip1: true,
      chip2: true,
      chip3: true,
      chip4: true,
      chip5: true,
    };
  }
};
</script>

<style scopd>
.tabs-block{background-color: #fff;padding: 5px 0px}
</style>