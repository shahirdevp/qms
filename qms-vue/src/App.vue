<template>
  <v-app>
    <navbar v-if="showMenu"></navbar>

    <v-content>
      <transition name="page" mode="out-in">
        <router-view></router-view>
      </transition>
    </v-content>
    <template>
      <v-footer class="pa-3">
        <v-spacer></v-spacer>
        <div>&copy; {{ new Date().getFullYear() }}</div>
      </v-footer>
    </template>
  </v-app>
</template>


<style scoped>
main {
  padding-top: 0px !important;
}
</style>

<style>
  .v-card { -webkit-box-shadow: 0px 0px 5px -2px rgba(0, 0, 0, 0.45), 2px 2px 10px 0px rgba(0, 0, 0, 0.14) !important; box-shadow: 0px 0px 5px -2px rgba(0, 0, 0, 0.45), 2px 2px 10px 0px rgba(0, 0, 0, 0.14) !important; text-decoration: none !important; }
  a { text-decoration: none; }
  html, body { overflow-y: auto; overflow-x:hidden; }
  /* #app{overflow-y:auto} */
  .page-enter-active, .page-leave-active { transition: opacity 0.6s, transform 0.5s; }
  .page-enter, .page-leave-to { opacity: 0; transform: translateX(-5%); }
  .action-bar { padding: 6px; border-top: 1px solid #d4d4d4; border-bottom: 1px solid #d4d4d4; background: #f7f7ff; }
  .page-name{line-height:35px;}
  .theme--light.v-btn-toggle .v-btn { color: rgba(0, 0, 0, 0.64); opacity: 1; }
  .card-table th{text-align: left; padding: 5px 10px; color: rgba(0,0,0); min-width: 200px; font-weight: 400;}
  .card-table td{padding: 5px 10px;color: rgba(0,0,0,0.7);}
  .custom-card-list{overflow-x: auto}
  .text-rr .v-select  { padding: 0; }
  .text-rr .v-input__slot{border-radius: 3px;}
  .text-rr .theme--light.v-text-field > .v-input__control > .v-input__slot::before { border-color: transparent; }
  .text-rr .v-input__append-inner { margin-top: -1px !important; }
  .text-rr input[type="date"], .text-rr input[type="number"] { padding: 0 12px; }
  .responsive-img{max-width: 100%;}
  /* card style */
  .card-box { background-color: #fefefe; padding: 15px; margin: 10px; border: 1px solid #f2f2f2; box-shadow: 0px 0px 3px -2px gray; width: calc(100% - 20px); }
  .card-box-title { color: #4b4b4b; font-size: 19px; margin-bottom: 10px; font-weight: 400; line-height: 1.5; }
  .cards-table th{ font-size: 14px; font-weight: 500; color: #1b1b1b; width: 150px; text-align: left; padding: 5px; }
</style>







<script>
import navbar from "./components/Common/Toolbar.vue";
import router from "./router";

export default {
  name: "App",
  components: {
    navbar
  },
  computed: {
    showMenu() {
      if (this.$route.name == "login" || this.$route.name == "register") {
        return false;
      } else {
        return true;
      }
    }
  },
  mounted() {
    this.$session.start();
    if (this.$session.has("token")) {
      // console.log(this.$session);
    }
  }
};
</script>
