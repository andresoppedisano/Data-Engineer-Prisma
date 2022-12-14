USE [master]
GO
/****** Object:  Database [Alkemy]    Script Date: 04/11/2022 20:05:51 ******/
CREATE DATABASE [Alkemy]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Alkemy', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\Alkemy.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Alkemy_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\Alkemy_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [Alkemy] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Alkemy].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Alkemy] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Alkemy] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Alkemy] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Alkemy] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Alkemy] SET ARITHABORT OFF 
GO
ALTER DATABASE [Alkemy] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Alkemy] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Alkemy] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Alkemy] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Alkemy] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Alkemy] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Alkemy] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Alkemy] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Alkemy] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Alkemy] SET  ENABLE_BROKER 
GO
ALTER DATABASE [Alkemy] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Alkemy] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Alkemy] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Alkemy] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Alkemy] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Alkemy] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Alkemy] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Alkemy] SET RECOVERY FULL 
GO
ALTER DATABASE [Alkemy] SET  MULTI_USER 
GO
ALTER DATABASE [Alkemy] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Alkemy] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Alkemy] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Alkemy] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Alkemy] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Alkemy] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Alkemy', N'ON'
GO
ALTER DATABASE [Alkemy] SET QUERY_STORE = OFF
GO
USE [Alkemy]
GO
/****** Object:  Table [dbo].[Alumno]    Script Date: 04/11/2022 20:05:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Alumno](
	[Legajo] [int] NOT NULL,
	[Nombre] [varchar](50) NULL,
	[Apellido] [varchar](50) NULL,
	[Fecha_de_Nacimiento] [varchar](25) NULL,
PRIMARY KEY CLUSTERED 
(
	[Legajo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cursa]    Script Date: 04/11/2022 20:05:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cursa](
	[Legajo] [int] NOT NULL,
	[Código_de_Materia] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Materia]    Script Date: 04/11/2022 20:05:51 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Materia](
	[Código] [int] NOT NULL,
	[Descripción] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[Código] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fecha_de_Nacimiento]) VALUES (1, N'Juan', N'López', N'13/09/1990')
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fecha_de_Nacimiento]) VALUES (2, N'Héctor', N'Fernandez', N'30/10/1980')
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fecha_de_Nacimiento]) VALUES (3, N'Lucas', N'Pérez', N'01/12/1995')
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fecha_de_Nacimiento]) VALUES (4, N'Mariano', N'Aimar', N'05/10/1992')
INSERT [dbo].[Alumno] ([Legajo], [Nombre], [Apellido], [Fecha_de_Nacimiento]) VALUES (5, N'Lucas', N'Álvarez', N'21/07/1985')
GO
INSERT [dbo].[Cursa] ([Legajo], [Código_de_Materia]) VALUES (1, 1)
INSERT [dbo].[Cursa] ([Legajo], [Código_de_Materia]) VALUES (2, 2)
INSERT [dbo].[Cursa] ([Legajo], [Código_de_Materia]) VALUES (3, 3)
INSERT [dbo].[Cursa] ([Legajo], [Código_de_Materia]) VALUES (4, 4)
INSERT [dbo].[Cursa] ([Legajo], [Código_de_Materia]) VALUES (5, 5)
GO
INSERT [dbo].[Materia] ([Código], [Descripción]) VALUES (1, N'Descripción')
INSERT [dbo].[Materia] ([Código], [Descripción]) VALUES (2, N'Descripción')
INSERT [dbo].[Materia] ([Código], [Descripción]) VALUES (3, N'Descripción')
INSERT [dbo].[Materia] ([Código], [Descripción]) VALUES (4, N'Descripción')
INSERT [dbo].[Materia] ([Código], [Descripción]) VALUES (5, N'Descripción')
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD  CONSTRAINT [fk_Código] FOREIGN KEY([Código_de_Materia])
REFERENCES [dbo].[Materia] ([Código])
GO
ALTER TABLE [dbo].[Cursa] CHECK CONSTRAINT [fk_Código]
GO
ALTER TABLE [dbo].[Cursa]  WITH CHECK ADD  CONSTRAINT [fk_Legajo] FOREIGN KEY([Legajo])
REFERENCES [dbo].[Alumno] ([Legajo])
GO
ALTER TABLE [dbo].[Cursa] CHECK CONSTRAINT [fk_Legajo]
GO
USE [master]
GO
ALTER DATABASE [Alkemy] SET  READ_WRITE 
GO
