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
        <h4 class="card-box-title">Organization</h4>
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

  </div>
</template>

<script>
import TabBlock from "../../components/Common/TabsBlock.vue";
export default {
  components: {
    TabBlock
  }
};
</script>