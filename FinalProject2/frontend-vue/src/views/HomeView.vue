<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to LeVehicles</p>
        <p class="subtitle">The best vehicle store online</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Promotions</h2>
      </div>
      <div class="promotion">
        <img
          class="promo-image"
          src="https://i.ibb.co/27n1Hff/banner-best-car-special-offer-3d-render.jpg"
          alt="banner-best-car-special-offer-3d-render"
          border="0"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ProductBox from "../components/ProductBox.vue";
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts();
    document.title = " Home | LeVehicles";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style>
.promotion {
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
}
.promo-image {
  width: 80%;
}
</style>
