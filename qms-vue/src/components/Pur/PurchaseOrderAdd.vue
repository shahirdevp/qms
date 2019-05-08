<template>
  <div id="empd">
    <v-layout row wrap class="action-bar">
      <v-flex xs6>
        <h3 class="page-name">Add New Purchase Order</h3>
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
              <label class="lab-for right black--text">Product</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.product" outline type="text"></v-text-field>
              </div>
            </v-flex>

             <v-flex md2>
              <label class="lab-for right black--text" >Unit</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.unit" outline type="text"></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Supplier ref no</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.supplier_ref_no" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Qty</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.qty" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Po no</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.po_no" outline></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Po date</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.po_date" outline type="date"></v-text-field>
              </div>
            </v-flex>

            <v-flex md2>
              <label class="lab-for right black--text">Requested date</label>
            </v-flex>
            <v-flex md4>
              <div class="text-rr">
                <v-text-field v-model="detail.requested_date" outline type="date"></v-text-field>
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
          .post(this.$apiUrl + "pur/purchase-order/", {
            supplier: this.detail.supplier,
            product: this.detail.product,
            unit: this.detail.unit,
            supplier_ref_no: this.detail.supplier_ref_no,
            qty: this.detail.qty,
            po_no: this.detail.po_no,
            po_date: this.detail.po_date,
            requested_date: this.detail.requested_date,
            owner: this.$owner
          })
          .then(function(response) {
            console.log(response.data);
            router.push("/purchase-order/" + response.data.id);
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
>>>input[type="date"] {
  padding: 0;
}
</style>
