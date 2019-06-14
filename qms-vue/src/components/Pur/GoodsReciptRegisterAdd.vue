<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Add New Goods Receipt Register</h3>
      </v-flex>
      <v-flex xs6>
        <div class="text-xs-right"></div>
      </v-flex>
    </v-layout>

    <!-- Insert-list-form -->
    <v-layout row class="lay-des1 white">
      <v-flex xs12 sm12 md11>
        <v-form ref="form" class v-model="valid" id="emp" lazy-validation>
          <v-layout class="white" row wrap>
            <v-flex md2>
              <label class="lab-for right black--text">Supplier</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
               <v-select
                  v-model="detail.supplier"
                  :items="supplier"
                  item-text="supplier"
                  item-value="id"
                ></v-select>
              </div>
            </v-flex>


             <v-flex md2>
              <label class="lab-for right black--text" >GRR No</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.grrno" outline type="text"></v-text-field>
              </div>
            </v-flex>
            

            <v-flex md2>
              <label class="lab-for right black--text">Dc ref</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.dc_ref" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Po ref </label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.po_ref" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Part</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.part" outline ></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Inward qty</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.inward_qty" outline ></v-text-field>
              </div>
            </v-flex>
            <v-flex md2>
              <label class="lab-for right black--text">Sup test report</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-textarea
                  v-model="detail.sup_test_report"
                  placeholder="Enter the value"
                  outline
                ></v-textarea>
              </div>
            </v-flex>
          </v-layout>

          
          <v-flex md12 offset-md2>
            <v-btn :disabled="!valid" color="success" @click="validate">Save</v-btn>
            <v-btn color="error" @click="reset">cancel</v-btn>
          </v-flex>
        </v-form>
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
      detail: [],
      valid: true,
      auditArea: []
    };
  },
  mounted() {
    this.getSupplier();
  },
  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        axios
          .post(this.$apiUrl + "pur/goods-recipt/", {
            supplier: this.detail.supplier,
            grrno: this.detail.grrno,
            dc_ref: this.detail.dc_ref,
            po_ref: this.detail.po_ref,
            part: this.detail.part,
            inward_qty: this.detail.inward_qty,
            sup_test_report: this.detail.sup_test_report,
            owner: this.$owner
          })
          .then(function(response) {
            console.log(response.data);
            router.push("goods-recipt-register/");
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    getSupplier() {
      var self = this;
      axios
        .get(this.$apiUrl + "pur/supplier/")
        .then(function(response) {
          self.supplier = response.data;
        })
        .catch(function(error) {
          console.log(error.data);
        });
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>

<style scoped>
.lab-for {
  line-height: 44px;
  margin-right: 8px;
}

</style>


