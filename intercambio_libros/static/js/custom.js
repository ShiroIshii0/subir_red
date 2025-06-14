<div class="formulario-registro d-flex align-items-center justify-content-center">
  <div class="container" style="max-width: 400px;">
    <h2 class="text-center mb-4">Registrarse</h2>

    <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit" class="btn btn-success w-100">Ingresar</button>
    </form>
  </div>
</div>
