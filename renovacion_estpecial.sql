-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.27-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla bd_renovacion_especial.laraigo_clasificaciones
CREATE TABLE IF NOT EXISTS `laraigo_clasificaciones` (
  `ticket` varchar(255) DEFAULT NULL,
  `fecha_ticket_hora_ticket` varchar(255) DEFAULT NULL,
  `fecha_fin` varchar(255) DEFAULT NULL,
  `hora_fin` varchar(255) DEFAULT NULL,
  `fecha_primera_interacion` varchar(255) DEFAULT NULL,
  `hora_primera_interacion` varchar(255) DEFAULT NULL,
  `persona` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `cerrado_por` varchar(255) DEFAULT NULL,
  `asesor` varchar(255) DEFAULT NULL,
  `tipo_cierre` varchar(255) DEFAULT NULL,
  `canal` varchar(255) DEFAULT NULL,
  `clasificacion_nivel_1` varchar(255) DEFAULT NULL,
  `clasificacion_nivel_2` varchar(255) DEFAULT NULL,
  `clasificacion_nivel_3` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla bd_renovacion_especial.laraigo_productividad_asesores
CREATE TABLE IF NOT EXISTS `laraigo_productividad_asesores` (
  `fecha` varchar(255) DEFAULT NULL,
  `usuario_del_asesor` varchar(255) DEFAULT NULL,
  `asesor` varchar(255) DEFAULT NULL,
  `hora_de_primer_logueo` varchar(255) DEFAULT NULL,
  `cantidad_de_tickets` varchar(255) DEFAULT NULL,
  `cerrados` varchar(255) DEFAULT NULL,
  `en_atencion` varchar(255) DEFAULT NULL,
  `suspendidos` varchar(255) DEFAULT NULL,
  `tme_promedio` varchar(255) DEFAULT NULL,
  `tme_maximo` varchar(255) DEFAULT NULL,
  `tme_minimo` varchar(255) DEFAULT NULL,
  `tmo_maximo` varchar(255) DEFAULT NULL,
  `tmo_minimo` varchar(255) DEFAULT NULL,
  `tmo_asesor_promedio` varchar(255) DEFAULT NULL,
  `tmo_asesor_maximo` varchar(255) DEFAULT NULL,
  `tmo_asesor_minimo` varchar(255) DEFAULT NULL,
  `tmr_promedio` varchar(255) DEFAULT NULL,
  `tmr_asesor` varchar(255) DEFAULT NULL,
  `minutos_conectados` varchar(255) DEFAULT NULL,
  `estado_actual` varchar(255) DEFAULT NULL,
  `grupo_de_atencion` varchar(255) DEFAULT NULL,
  `break` varchar(255) DEFAULT NULL,
  `backoffice` varchar(255) DEFAULT NULL,
  `coaching` varchar(255) DEFAULT NULL,
  `feedback` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla bd_renovacion_especial.laraigo_tickets
CREATE TABLE IF NOT EXISTS `laraigo_tickets` (
  `ticket` varchar(255) DEFAULT NULL,
  `canal` varchar(255) DEFAULT NULL,
  `persona` varchar(255) DEFAULT NULL,
  `origen` varchar(255) DEFAULT NULL,
  `grupo_inicial_del_ticket` varchar(255) DEFAULT NULL,
  `grupo_final_del_ticket` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `fecha_de_inicio` varchar(255) DEFAULT NULL,
  `fecha_de_fin` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `tipo_de_cierre` varchar(255) DEFAULT NULL,
  `tiempo_real` varchar(255) DEFAULT NULL,
  `tiempo_pausado` varchar(255) DEFAULT NULL,
  `tiempo_total_tmo` varchar(255) DEFAULT NULL,
  `fecha_de_derivacion` varchar(255) DEFAULT NULL,
  `fecha_de_ultima_interaccion` varchar(255) DEFAULT NULL,
  `agente_inicial` varchar(255) DEFAULT NULL,
  `agente_final` varchar(255) DEFAULT NULL,
  `rol_del_agente` varchar(255) DEFAULT NULL,
  `supervisor` varchar(255) DEFAULT NULL,
  `empresa` varchar(255) DEFAULT NULL,
  `campana` varchar(255) DEFAULT NULL,
  `tmo_asesor` varchar(255) DEFAULT NULL,
  `tiempo_medio_de_respuesta_tmr` varchar(255) DEFAULT NULL,
  `tiempo_medio_de_respuesta_asesor_tm` varchar(255) DEFAULT NULL,
  `tiempo_primera_respuesta_asesor_tme` varchar(255) DEFAULT NULL,
  `tiempo_medio_de_respuesta_cliente_t` varchar(255) DEFAULT NULL,
  `primera_asignacion` varchar(255) DEFAULT NULL,
  `tiempo_de_espera_antes_de_atencion_` varchar(255) DEFAULT NULL,
  `tiempo_de_espera_en_holding` varchar(255) DEFAULT NULL,
  `clasificacion` varchar(255) DEFAULT NULL,
  `tipo_de_documento` varchar(255) DEFAULT NULL,
  `numero_de_documento` varchar(255) DEFAULT NULL,
  `correo_electronico` varchar(255) DEFAULT NULL,
  `n_balanceos` varchar(255) DEFAULT NULL,
  `abandono` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `tiempo_de_supervision_de_llamada` varchar(255) DEFAULT NULL,
  `fecha_de_publicacion_original` varchar(255) DEFAULT NULL,
  `cantidad_de_seguidores` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- La exportación de datos fue deseleccionada.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
