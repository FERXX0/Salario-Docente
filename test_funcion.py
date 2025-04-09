import unittest
from funcion import calcular_salario

class testcalcular_salario(unittest.TestCase):

    def test_tipo_contrato_invalido(self):
        resultado = calcular_salario('Parcial', 10, 5, 3, 2)
        self.assertEqual(resultado, "Error: Tipo de contrato no válido")

    def test_horas_diurnas_negativas(self):
        resultado = calcular_salario('docente_tc', -5, 4, 2, 1)
        self.assertEqual(resultado, "Error: Horas no pueden ser negativas")

    def test_horas_nocturnas_negativas(self):
        resultado = calcular_salario('docente_mc', 8, -3, 1, 0)
        self.assertEqual(resultado, "Error: Horas no pueden ser negativas")

    def test_horas_dominicales_negativas(self):
        resultado = calcular_salario('docente_tc', 6, 4, -2, 2)
        self.assertEqual(resultado, "Error: Horas no pueden ser negativas")

    def test_horas_festivas_negativas(self):
        resultado = calcular_salario('docente_mc', 7, 3, 2, -1)
        self.assertEqual(resultado, "Error: Horas no pueden ser negativas")

    def test_valores_no_numericos(self):
        resultado = calcular_salario('docente_tc', 'cinco', 4, 2, 1)
        self.assertEqual(resultado, "Error: Las horas deben ser números")

    def test_calculo_salario_bruto(self):
        resultado = calcular_salario('docente_tc', 40, 10, 5, 2)
        self.assertEqual(resultado["Salario Bruto"], 3350000)

    def test_descuento_parafiscales(self):
        resultado = calcular_salario('docente_mc', 35, 8, 4, 1)
        self.assertAlmostEqual(resultado["Descuento Parafiscales"], resultado["Salario Bruto"] * 0.09)

    def test_salario_neto_correcto(self):
        resultado = calcular_salario('docente_tc', 30, 5, 3, 2)
        self.assertAlmostEqual(resultado["Salario Neto"], resultado["Salario Bruto"] * 0.91)

    def test_docente_sin_horas(self):
        resultado = calcular_salario('docente_tc', 0, 0, 0, 0)
        self.assertEqual(resultado["Salario Bruto"], 0)

    def test_solo_horas_diurnas(self):
        resultado = calcular_salario('docente_mc', 40, 0, 0, 0)
        self.assertEqual(resultado["Salario Bruto"], 1200000)

    def test_solo_horas_nocturnas(self):
        resultado = calcular_salario('docente_tc', 0, 10, 0, 0)
        self.assertEqual(resultado["Salario Bruto"], 700000)

    def test_solo_horas_dominicales(self):
        resultado = calcular_salario('docente_mc', 0, 0, 5, 0)
        self.assertEqual(resultado["Salario Bruto"], 350000)

    def test_solo_horas_festivas(self):
        resultado = calcular_salario('docente_tc', 0, 0, 0, 3)
        self.assertEqual(resultado["Salario Bruto"], 300000)

    def test_combinaciones_de_horas(self):
        resultado = calcular_salario('docente_mc', 20, 10, 5, 2)
        self.assertGreater(resultado["Salario Bruto"], 0)

    def test_valores_extremos(self):
        resultado = calcular_salario('docente_tc', 1000, 500, 300, 200)
        self.assertGreater(resultado["Salario Bruto"], 0)

    def test_tarifas_medio_tiempo(self):
        resultado = calcular_salario('docente_mc', 20, 5, 3, 2)
        self.assertGreater(resultado["Salario Bruto"], 0)

    def test_tarifas_tiempo_completo(self):
        resultado = calcular_salario('docente_tc', 30, 8, 4, 2)
        self.assertGreater(resultado["Salario Bruto"], 0)

    def test_formato_separador_miles(self):
        resultado = calcular_salario('docente_tc', 50, 15, 7, 3)
        self.assertIsInstance(resultado["Salario Bruto"], int)

    def test_mezcla_horas_correcta(self):
        resultado = calcular_salario('docente_mc', 25, 10, 5, 2)
        self.assertGreater(resultado["Salario Bruto"], 0)


if __name__ == '__main__':
    unittest.main()