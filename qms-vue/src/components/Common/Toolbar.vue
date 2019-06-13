<template>
    <div>
        <v-navigation-drawer persistent :mini-variant="miniVariant" :clipped="clipped" v-model="drawer" enable-resize-watcher fixed app>
<!--            <v-list>-->
<!--                <router-link v-for="(item, i) in items" :key="i" :to="item.link">-->
<!--                    <v-tooltip right>-->
<!--                        <template v-slot:activator="{ on }">-->
<!--                            <v-list-tile value="true" class="hov-back">-->
<!--                                <v-list-tile-action dark v-on="on">-->
<!--                                    <v-icon v-html="item.icon"></v-icon>-->
<!--                                </v-list-tile-action>-->
<!--                                <v-list-tile-content>-->
<!--                                    <v-list-tile-title v-text="item.title" class="black&#45;&#45;text"></v-list-tile-title>-->
<!--                                </v-list-tile-content>-->
<!--                            </v-list-tile>-->
<!--                        </template>-->
<!--                        <span v-html="item.tip"></span>-->
<!--                    </v-tooltip>-->
<!--                </router-link>-->
<!--            </v-list>-->
            <v-list>
                <v-list-tile to="dashboard">
                    <v-list-tile-action>
                        <v-icon>dashboard</v-icon>
                    </v-list-tile-action>
                    <div class="subheading-set" v-if="miniVariant == true">Dashboard</div>
                    <v-list-tile-title>Dashboard</v-list-tile-title>
                </v-list-tile>


                <v-list-group
                        v-for="item in items"
                        :key="item.title"
                        v-model="item.active"
                        :prepend-icon="item.action"
                        no-action
                        @click="miniVariant = false"
                >

                    <template v-slot:activator>
                        <div class="subheading-set" v-if="miniVariant == true">{{ item.title }}</div>
                        <v-list-tile>
                            <v-list-tile-content>
                                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </template>


                    <v-list-tile
                            v-for="subItem in item.items"
                            :key="subItem.title"
                            :to="subItem.routs"
                    >
                        <v-list-tile-content>
                            <v-list-tile-title>{{ subItem.title }}</v-list-tile-title>
                        </v-list-tile-content>

                        <v-list-tile-action>
                            <v-icon>{{ subItem.action }}</v-icon>
                        </v-list-tile-action>
                    </v-list-tile>
                </v-list-group>


            </v-list>
        </v-navigation-drawer>
        <v-toolbar app :clipped-left="clipped">
            <v-toolbar-side-icon @click="sliderCloser"></v-toolbar-side-icon>
<!--            <v-btn icon @click.stop="miniVariant = !miniVariant">-->
<!--                <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>-->
<!--            </v-btn>-->
<!--            <v-btn icon @click.stop="clipped = !clipped">-->
<!--                <v-icon>web</v-icon>-->
<!--            </v-btn>-->

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
      clipped: false,
      drawer: true,
      fixed: true,
      miniVariant: false,
      right: false,
      rightDrawer: false,
      title: "Vuetify.js",

        items: [
            {
                action: 'person',
                title: 'HR',
                active: false,
                items: [
                    { title: 'Requirement register', routs:'hr-list', action:'' },
                    { title: 'Employee data', routs:'employee' , action:''},
                    { title: 'Competency matrix', routs:'compentency-matrix', action:'' },
                    { title: 'Training request register', routs:'trining-request-register', action:'' },
                    { title: 'Annual training plan', routs:'anual-training-plan', action:'' },
                    { title: 'Training evaluation record', routs:'training-evalution-record', action:'' },
                    { title: 'Skill Matrix', routs:'skill-matrix', action:'' },

                ]
            },
            {
                action: 'bar_chart',
                title: 'Marketing',
                items: [
                    { title: 'Enquiry register', routs:'marketing-enquiry', action:'' },
                    { title: 'Technical Feasibility', routs:'technical-feasiblity', action:'' },
                    { title: 'Quality Feasibility', routs:'quality-feasibility', action:'' },
                    { title: 'Marketing Feasibility', routs:'marketing-feasibility', action:'' },
                    { title: 'Reviewer', routs:'reviewer', action:'' },
                    { title: 'Configuration Management', routs:'configration-management', action:'' },
                ]
            },
            {
                action: 'vertical_split',
                title: 'MR',
                items: [
                    { title: 'Document Type', routs:'mr-doc-type', action:'' },
                    { title: 'Internal External doc', routs:'mr-internal-external-docs', action:'' },
                    { title: 'Internal audit plan', routs:'mr-internal-audit-plan', action:'' },
                    { title: 'Internal audit report', routs:'mr-internal-audit-report', action:'' },
                    { title: 'Non conformance', routs:'mr-non-conformance', action:'' },
                ]
            },
            {
                action: 'list_alt',
                title: 'Purchase order',
                items: [
                    { title: 'Suppliers', routs:'suppliers', action:'' },
                    { title: 'Approved suppliers', routs:'purchase-approved-supplier', action:'' },
                    { title: 'Supplier purchase order', routs:'purchase-order', action:'' },
                    { title: 'Goods receipt register', routs:'goods-recipt-register', action:'' },
                    { title: 'Stock register', routs:'stock-register', action:'' },
                ]
            },

            {
                action: 'settings',
                title: 'Settings',
                items: [
                    { title: 'Organization Process', routs:'org-chart', action:'' },
                    { title: 'Organization Settings', routs:'org-settings', action:'' },
                ]
            }
        ]
    };
  },

  methods:{
      sliderCloser (){
          for(var item in this.items){
              if(this.items[item].active == true){
                  this.items[item].active = false
              }
          }
        this.miniVariant = !this.miniVariant;

      },
    },
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

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #d8d8d8;
}

::-webkit-scrollbar-thumb {
    background: #909090;
    border-radius:10px
}

::-webkit-scrollbar-thumb:hover {
    background: #555;
}

.v-navigation-drawer{
    scrollbar-width:thin;
}

.subheading-set {
    position: absolute;
    width: 100%;
    text-align: center;
    left: 0;
    top: 35px;
    color: gray;
    font-size: 10px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    padding: 0px 10px;
}

</style>
