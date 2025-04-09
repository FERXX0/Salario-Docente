def calcular_salario(tipo_contrato, horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas):

    # Validar que todas las horas sean números
    if not all(isinstance(h, (int, float)) for h in [horas_diurnas, horas_nocturnas, horas_dominicales, horas_festivas]):
        return "Error: Las horas deben ser números"

    # Validar que no haya horas negativas
    if horas_diurnas < 0 or horas_nocturnas < 0 or horas_dominicales < 0 or horas_festivas < 0:
        return "Error: Horas no pueden ser negativas"

    tarifas = {
        "docente_tc": {"diurna": 50000, "nocturna": 70000, "dominical": 90000, "festiva": 100000},
        "docente_mc": {"diurna": 30000, "nocturna": 50000, "dominical": 70000, "festiva": 80000},
    }

    if tipo_contrato not in tarifas:
        return "Error: Tipo de contrato no válido"

    t = tarifas[tipo_contrato]

    salario_bruto = (
        horas_diurnas * t["diurna"] +
        horas_nocturnas * t["nocturna"] +
        horas_dominicales * t["dominical"] +
        horas_festivas * t["festiva"]
    )

    descuento = salario_bruto * 0.09
    salario_neto = salario_bruto - descuento

    def redondear(valor):
        return int(valor) if valor == int(valor) else round(valor, 2)

    return {
        "Salario Bruto": redondear(salario_bruto),
        "Descuento Parafiscales": redondear(descuento),
        "Salario Neto": redondear(salario_neto)
    }

if __name__ == "__main__":
    resultado = calcular_salario("docente_tc", 40, 10, 5, 2)
    print(resultado)