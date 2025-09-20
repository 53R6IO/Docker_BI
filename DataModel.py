from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
# Jugador,Nacionalidad,Posicion,Edad,Dia_partido,Goles,Tiros Totales,xG,npxG,xAG,xAG,Acciones_que_crean_tiros,Pases_intentados,Pases_intentados,Pases_intentados,Pases_progresivos,Pases_progresivos,Regates_exitosos,Regates_exitosos,Pases_medios_completados,Pases_largos_completados,xAG,xAG,xA,Pases_en_ultimo_tercio,Pases_balon_vivo,Pases_balon_muerto,Pases_al_hueco,Pases_centros,Pases_completados,Pases_completados,Pases_completados,Pases_fuera_de_juego,Valla_no_vencida,Errores_defnsivos_ocasion_tiro,Toques_en_zona_ofensiva,Toques_en_area_rival,%_de_regates_exitosos,Veces_que_fue_barrido_regate,Acarreos_ultimo_tercio,Malos_controles,Perdida_balon,Pases_recibidos,Pases_progresivos_recibidos,Faltas_cometidas,Centros,Duelos_aereos_ganados,%_de_duelos_aereos_ganados,contract_date

    Jugador: str
    Nacionalidad: str
    Posicion: str
    Edad: str
    Dia_partido: str
    Goles: int
    Tiros_Totales: int
    xG: float
    npxG: float
    xAG: float
    xAG_2: float
    Acciones_que_crean_tiros: int
    Pases_intentados_1: int
    Pases_intentados_2: int
    Pases_intentados_3: int
    Pases_progresivos_1: int
    Pases_progresivos_2: int
    Regates_exitosos_1: int
    Regates_exitosos_2: int
    Pases_medios_completados: int
    Pases_largos_completados: int
    xAG_3: float
    xAG_4: float
    xA: float
    Pases_en_ultimo_tercio: int
    Pases_balon_vivo: int
    Pases_balon_muerto: int
    Pases_al_hueco: int
    Pases_centros: int
    Pases_completados_1: int
    Pases_completados_2: int
    Pases_completados_3: int
    Pases_fuera_de_juego: int
    Valla_no_vencida: int
    Errores_defnsivos_ocasion_tiro: int
    Toques_en_zona_ofensiva: int
    Toques_en_area_rival: int
    Porc_de_regates_exitosos: float
    Veces_que_fue_barrido_regate: int
    Acarreos_ultimo_tercio: int
    Malos_controles: int
    Perdida_balon: int
    Pases_recibidos: int
    Pases_progresivos_recibidos: int
    Faltas_cometidas: int
    Centros: int
    Duelos_aereos_ganados: int
    Porc_de_duelos_aereos_ganados: float
    contract_date: str

#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["Jugador", "Nacionalidad", "Posicion", "Edad", "Dia_partido", "Goles", "Tiros Totales", "xG", "npxG", "xAG", "xAG_2", "Acciones_que_crean_tiros", "Pases_intentados_1", "Pases_intentados_2", "Pases_intentados_3", "Pases_progresivos_1", "Pases_progresivos_2", "Regates_exitosos_1", "Regates_exitosos_2", "Pases_medios_completados", "Pases_largos_completados", "xAG_3", "xAG_4", "xA", "Pases_en_ultimo_tercio", "Pases_balon_vivo", "Pases_balon_muerto", "Pases_al_hueco", "Pases_centros", "Pases_completados_1", "Pases_completados_2", "Pases_completados_3", "Pases_fuera_de_juego", "Valla_no_vencida", "Errores_defnsivos_ocasion_tiro", "Toques_en_zona_ofensiva", "Toques_en_area_rival", "%_de_regates_exitosos", "Veces_que_fue_barrido_regate", "Acarreos_ultimo_tercio", "Malos_controles", "Perdida_balon", "Pases_recibidos", "Pases_progresivos_recibidos", "Faltas_cometidas", "Centros", "Duelos_aereos_ganados", "%_de_duelos_aereos_ganados", "contract_date"]
