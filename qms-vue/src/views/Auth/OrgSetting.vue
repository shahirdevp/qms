<template>
  <div>
    <TabBlock/>
    <v-layout row wrap class="action-bar">
        <v-flex xs6>
            <h3 class="page-name">Organization Settings</h3>
        </v-flex>
        <v-flex xs6>
            <div class="text-xs-right"></div>
        </v-flex>
    </v-layout>

    <div class="card-box">
        <h4 class="card-box-title">Organization Detail</h4>
        <table class="cards-table">
            <tr>
                <th>Name</th>
                <td>5ine websolution</td>
            </tr>
            <tr>
                <th>Address</th>
                <td>    
                    Flat No - S2(2nd floor),
                    Site No - 592, 60 Feet Road BEML Layout 4th Stage,
                    Rajarajeshwari Nagar Bangalore - 560098
                    Landmark: Udaya Ravi Eye Hospital Road.
                </td>
            </tr>
            <tr>
                <th>Scope</th>
                <td>A hearty welcome to 5ine’s, It is a global leader in offering Online solutions, Technology solutions, Business Solutions and many more. </td>
            </tr>
            <tr>
                <th>Policy</th>
                <td>Some document</td>
            </tr>
            <tr>
                <th>CEO</th>
                <td>Santhosh B S</td>
            </tr>
        </table>

    </div>

    <div class="card-box">
        <h4 class="card-box-title">Organization Process</h4>
            <v-layout wrap row>

                <v-flex xs12 sm3 md3  class="mb-2  pa-3" v-for="item in process" :key="item.title" >
                    <v-card color="light-blue darken-3" class="white--text" >
                        <v-card-title primary-title>
                            <div>
                            <div class="headline">{{ item.title }}</div>
                             <span>{{ item.subtitle }}</span>
                             <div><router-link to="" class="hlink">{{ item.head }}</router-link></div>
                            </div>
                        </v-card-title>
                        <v-card-actions>
                             <v-btn @click.stop="dialog = !dialog"   flat dark><v-icon small left dark>edit</v-icon>Edit </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>

               
            </v-layout>
        
    </div>
    <template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" persistent max-width="450px">
        
        <v-card>
            <v-card-text>
            <v-container class="mt-0" row grid-list-md>
                <v-layout wrap>
                    <span class="headline">User Profile</span>
                <v-flex xs12>
                    <v-text-field label="Short Title*" required></v-text-field>
                </v-flex>
                <v-flex xs12>
                    <v-text-field label="Full title" required></v-text-field>
                </v-flex>
                <v-flex xs12 sm12>
                    <v-autocomplete
                    :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                    label="Select Team Manager"
                    ></v-autocomplete>
                </v-flex>
                </v-layout>
            </v-container>
            </v-card-text>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="dialog = false">Cancle</v-btn>
            <v-btn color="blue darken-1" flat @click="dialog = false">Update</v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>
    </v-layout>
    </template>

  </div>
</template>

<script>
import TabBlock from "../../components/Common/TabsBlock.vue";
export default {
  components: {
    TabBlock
  },
   data: () => ({
      dialog: false,
      process:[
        {
          title:"HR",
          subtitle:'Human resource',
          head:'Human resource head',
          img:'',
          color:'',
        },
        {
          title:"MKT",
          subtitle:'Marketing',
          head:'Marketing head',
          img:'',
          color:'',
        },
        {
          title:"MR",
          subtitle:'Master list',
          head:'Master list head',
          img:'',
          color:'',
        },
        {
          title:"PRD",
          subtitle:'Production',
          head:'Production head',
          img:'',
          color:'',
        },
        {
          title:"PUR",
          subtitle:'Purchase',
          head:'Purchase head',
          img:'',
          color:'',
        },
        {
          title:"QCD",
          subtitle:'Quality check',
          head:'Quality check head',
          img:'',
          color:'',
        },
      ]
    })
};
</script>

<style scoped>
    .hlink{
        color:#c3c3c3
    }
    .hlink:hover{
        color:#fff;
        transform: scale(1.1);
    }
</style>
