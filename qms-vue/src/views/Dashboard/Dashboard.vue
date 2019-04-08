<template>
     <v-container grid-list-md text-xs-center fluid>
         <v-layout row wrap>
            <service />
         </v-layout>
     </v-container>
</template>

<script>
import service from "../../components/Dashboard/Services.vue";
export default {
    name :'Dashboard',
    components: {
        service
    },
}
</script>