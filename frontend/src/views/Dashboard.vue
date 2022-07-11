<template>
<div>
   <v-row no-gutters style="margin-top:30px">
      <Header/>
    </v-row>
    <v-row no-gutters>
      <v-col
        v-for="card in cards"
        :key="card.title"
        cols="12"
        sm="4"
      >
      <v-card elevation="2"
       class="mx-auto"
       style="height:200px; background:#efedf5">
       <v-card-title v-text="card.title"></v-card-title>
       </v-card>
      </v-col>
    </v-row>
</div>
</template>

<script>
import Header from '../components/Header.vue'
  export default {
    components:{Header},
    data: () => ({
      items: ['foo', 'bar', 'fizz', 'new'],
      values: ['foo', 'bar'],
      value: null,
      cards: [
        { title: 'Data Sets Lookup', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: 'Models Lookup', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'YAML File', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
    }),
  }
</script>