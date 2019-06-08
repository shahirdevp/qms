<template>
    <div>
        <v-navigation-drawer persistent :mini-variant="miniVariant" :clipped="clipped" v-model="drawer" enable-resize-watcher fixed app>
            <v-list>
                <router-link v-for="(item, i) in items" :key="i" :to="item.link">
                    <v-tooltip right>
                        <template v-slot:activator="{ on }">
                            <v-list-tile value="true" class="hov-back">
                                <v-list-tile-action dark v-on="on">
                                    <v-icon v-html="item.icon"></v-icon>
                                </v-list-tile-action>
                                <v-list-tile-content>
                                    <v-list-tile-title v-text="item.title" class="black--text"></v-list-tile-title>
                                </v-list-tile-content>
                            </v-list-tile>
                        </template>
                        <span v-html="item.tip"></span>
                    </v-tooltip>
                </router-link>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar app :clipped-left="clipped">
            <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-btn icon @click.stop="miniVariant = !miniVariant">
                <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
            </v-btn>
            <v-btn icon @click.stop="clipped = !clipped">
                <v-icon>web</v-icon>
            </v-btn>

            <v-spacer></v-spacer>
            <v-btn icon @click.stop="rightDrawer = !rightDrawer">
                <v-icon>menu</v-icon>
            </v-btn>
        </v-toolbar>
        <v-content></v-content>
        <v-navigation-drawer temporary :right="right" v-model="rightDrawer" fixed app>
            <v-list>
                <v-list-tile @click="right = !right">
                    <v-list-tile-action>
                        <v-icon>compare_arrows</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title>Switch drawer (click me)</v-list-tile-title>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <!-- end menu bar -->
    </div>
</template>

<script>
export default {
  data() {
    return {
      clipped: true,
      drawer: true,
      fixed: true,
      items: [
                {
          icon: "dashboard",
          title: "Dashboard",
          link: "dashboard",
          tip:"Dashboard",
        },
        {
          icon: "person",
          title: "Hr",
          link: "hr",
          tip:"Hr",
        },
        {
          icon: "local_library",
          title: "Emplooyee Data",
          link: "employee",
          tip:"Emplooyee Data",
        },
                {
          icon: "iso",
          title: "Compentency Matrix",
          link: "compentency-matrix",
          tip:"Compentency Matrix",
        },
        {
          icon: "sync",
          title: "Training Request",
          link: "training-request",
          tip:"Training Request",
        },
                {
          icon: "beenhere",
          title: "Annual Training",
          link: "anual-training-plan",
          tip:"Annual Training",
        },
                {
          icon: "insert_drive_file",
          title: "Training Attendance",
          link: "training-attendance",
          tip:"Training Attendance",

        },
                {
          icon: "merge_type",
          title: "Training Evaluation",
          link: "training-evalution-record",
          tip:"Training Evaluation",
        },
                {
          icon: "insert_chart_outlined",
          title: "Skill Matrix",
          link: "skill-matrix",
          tip:"Skill Matrix",

          
        },
      ],
      miniVariant: false,
      right: false,
      rightDrawer: false,
      title: "Vuetify.js"
    };
  }
};
</script>

<style>
.hov-back:hover {
    background: #eaeaea;
}
.v-toolbar {
  -webkit-box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.07),
    0px 4px 5px 0px rgba(0, 0, 0, 0), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
  box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.07),
    0px 4px 5px 0px rgba(0, 0, 0, 0), 0px 1px 10px 0px rgba(0, 0, 0, 0.12);
}
</style>
