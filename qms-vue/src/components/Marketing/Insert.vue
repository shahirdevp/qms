<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">CREATE MARKETING ENQUIRY</h3>
      </v-flex>
      <v-flex xs6>
        <!-- <div class="text-xs-right">
          <div :class="{dn : !dn}">
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="info">edit</v-icon>
                </v-btn>
              </template>
              <span>Edit</span>
            </v-tooltip>
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="deleteData()">
                  <v-icon color="red">delete</v-icon>
                </v-btn>
              </template>
              <span>Delete</span>
            </v-tooltip>
          </div>

          <div :class="{dn : dn}">
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click.stop="dn = !dn">
                  <v-icon color="warning">close</v-icon>
                </v-btn>
              </template>
              <span>Cancel</span>
            </v-tooltip>
            <v-tooltip v-model="show" bottom>
              <template v-slot:activator="{ on }">
                <v-btn icon v-on="on" ref="fileInput" @click="validate()">
                  <v-icon color="success">check</v-icon>
                </v-btn>
              </template>
              <span>Save</span>
            </v-tooltip>
          </div>
        </div> -->
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout container>
      <v-flex xs12 sm12 md12>
        <v-card>
          <v-form ref="form" v-model="valid" id="emp" lazy-validation>
            <v-layout class="lay-des-pad primary" row wrap>
              <v-flex xs12>
                <h3 class="head white--text">MARKETING ENQUIRY </h3>
              </v-flex>
            </v-layout>
            <!-- <div class="under-line"></div> -->
            <v-layout class="lay-des1 white" row wrap>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Customer Name</label>
                  <v-text-field v-model="detail.name" placeholder="Customer Name" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Contact</label>
                  <v-text-field v-model="detail.contact" placeholder="Contact" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Line No</label>
                  <v-text-field v-model="detail.lineNo" placeholder="Line No" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Part Number</label>
                  <v-text-field v-model="detail.partNo" placeholder="Part Number" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Description</label>
                  <v-text-field v-model="detail.des" placeholder="Description" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Drawing Number</label>
                  <v-text-field v-model="detail.drawNo" placeholder="Drawing Number" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Qty</label>
                  <v-text-field v-model="detail.qty" placeholder="Qty" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Quotation Ref</label>
                  <v-text-field v-model="detail.quotRef" placeholder="Quotation Ref" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Date</label>
                  <v-text-field v-model="detail.date" placeholder="Date" outline></v-text-field>
                </div>
              </v-flex>
			  <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">PO NO</label>
                  <v-text-field v-model="detail.pono" placeholder="PO NO" outline></v-text-field>
                </div>
              </v-flex>
              <v-flex md3>
                <div class="text-rr">
                  <label class="lab-for grey--text">Status</label>
                  <v-select
                    class="field-sp"
                    v-model="detail.status"
                    :items="s1"
                    outline
                    placeholder="Status"
                  ></v-select>
                </div>
              </v-flex>
              <v-flex md12>
                <v-btn :disabled="!valid" color="success" @click="validate">Save</v-btn>
                <v-btn color="error" @click="reset">cancel</v-btn>
              </v-flex>
            </v-layout>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import swal from "sweetalert2";
import router from "../../router";

export default {
  data() {
    return {
      valid: true,
      detail: [],
      s1:['Not Awarded','Awarded','Not In Scope','Pending'],
    };
  },
  methods: {
     validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        axios.post(this.$apiUrl+'mkt/enquery-register/', {
            customer : this.detail.name,
            date : this.detail.date,
            prodeliverDate : this.date,
            contact : this.detail.contact,
            contryCode : '+91',
            line_number : this.detail.lineNo,
            partNumber : this.detail.partNo,
            description : this.detail.des,
            drawingNumber : this.detail.drawNo,
            qty : this.detail.qty,
            quotationRef : this.detail.quotRef,
            status : this.detail.status,
            poNumber : this.detail.pono,
            owner : this.$owner,
        })
        .then(function (response) {
            router.push("/marketing-enquiry/"+response.data.id);
        })
        .catch(function (error) {
            console.log(error);
        });
      }
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>

<style scoped>
.two-column {
  column-count: 2;
  column-gap: 15px;
}
.three-column {
  column-count: 3;
  column-gap: 15px;
}
</style>
