<template>
<v-container grid-list-md text-xs-center fluid>
  <v-layout align-content-center>
    <v-flex xs6 sm4 md3 value="true" v-for="(item, i) in serviceList" :key="i" >
      <router-link :to="item.link" class="a-link">
        <v-card>
             <v-card-title class="justify-center circle">
                <v-icon v-html="item.icon"></v-icon>
             </v-card-title>
            <v-card-text v-text="item.title">df</v-card-text>
        </v-card><!-- end card -->
      </router-link>
    </v-flex><!-- end service -->
  </v-layout>
</v-container>
</template>

<style scoped>
  .justify-center{justify-content: center;}
  .circle .v-icon{width: 75px; height: 75px; border-radius: 50%; -webkit-box-shadow: 1px 1px 5px #7e7878; box-shadow: 0px 0px 29px -17px #617cda; font-size: 30px; line-height: 75px; color: #617cda;}
  .v-card__text { font-size: 14px; letter-spacing: 1px; font-weight: 700; }
  .a-link:hover .v-card{ transform: scale(1.05); z-index: 1; }
  .v-card { min-height: 202px; }
</style>




<script>
export default {
    name:'subcategory',
  data(){
    return {
      serviceList:[
        { icon : 'person_outline', title : 'Document Type', link : '/mr-doc-type' },
        { icon : 'polymer', title : 'Internal External Docs', link : '/mr-internal-external-docs' },
        { icon : 'announcement', title : 'Internal Audit Plan', link : '/mr-internal-audit-plan' },
        { icon : 'cached', title : 'Internal Audit Report', link : '/mr-internal-audit-report' },
        { icon : 'description', title : 'Non conformance', link : '/mr-non-conformance' },
       								
      ]
    }
  }
}
</script>